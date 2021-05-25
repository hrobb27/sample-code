  
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#define MAXCHARS 1024
void handle_int(){
  char *st = "\ncaught sigint\nCS341 >";
  write(STDOUT_FILENO, st, 22);
}
void handle_stp(){
  char *st = "\ncaught sigtstp\nCS341 >";
  write(STDOUT_FILENO, st, 23);
}
int execute_funct(char **args, char **args2, int mode){
  pid_t pid;
  pid_t pid2;
  pid_t daddypid;
  pid_t daddypid2;
  int status;
  int status2;
  int fd[2];
  if (pipe(fd) == -1){
    printf("something astonishing has occured\n");
    exit(EXIT_FAILURE);
  };
  pid = fork();
  if (pid == 0){
    if(mode == 1){
      dup2(fd[1], STDOUT_FILENO); //set process' stdout to go to fd...
      close(fd[0]);
      close(fd[1]);
    }
    execvp(args[0], args);
    exit(EXIT_FAILURE);
  }else if (pid < 0){
    printf("forking just straight up didn't work\n");
  }else{
    if(mode == 1){
      pid2 = fork();
      if (pid2 == 0){
        dup2(fd[0], STDIN_FILENO);
        close(fd[0]);
        close(fd[1]);
        execvp(args2[0], args2);
        exit(EXIT_FAILURE);
      }else if (pid2 < 0){
        printf("something horrible has happened\n");
        exit(EXIT_FAILURE);
      }else{
        close(fd[0]);
        close(fd[1]);
        daddypid2 = wait(&status2);
        if(WIFEXITED(status2)){
          printf("pid:%d exit value:%d\n", daddypid2, WEXITSTATUS(status2));
        }else if(WIFSIGNALED(status)){
          printf("pid:%d signal:%d\n", daddypid2, WTERMSIG(status));
        }
      }
    }else if(mode == 2){
      pid2 = fork();
      if (pid2 == 0){
        close(fd[0]);
        close(fd[1]);
        execvp(args2[0], args2);
        exit(EXIT_FAILURE);
      }else if(pid < 0){
        printf("Something horrible has happened\n");
        exit(EXIT_FAILURE);
      }else{
        daddypid2 = wait(&status2);
        if(WIFEXITED(status2)){
          printf("pid:%d exit value:%d\n", daddypid2, WEXITSTATUS(status2));
        }else if (WIFSIGNALED(status)){//inductive hypothesis: the signal handler did the right stuff
          printf("pid:%d signal:%d\n", daddypid2, WTERMSIG(status));
        }
      }
    }
    close(fd[0]);
    close(fd[1]);
    daddypid = wait(&status);
    if(WIFEXITED(status)){
      printf("pid:%d exit value:%d\n", daddypid, WEXITSTATUS(status));
    }else if (WIFSIGNALED(status)){
      printf("pid:%d signal:%d\n", daddypid, WTERMSIG(status));
    }
  }
  return 1;
}
int betterparseline(char *line){
  char *token;
  char *cmd1[MAXCHARS];
  char *cmd2[MAXCHARS];
  size_t cmd1s = 0;
  size_t cmd2s = 0;
  int mode = 0;
  int i = 0;
  int l = 0;
  char tmp;
  char *end1;
  int foundstuff = 0;
  token = strtok_r(line, " ", &end1);
  while(token != NULL){
    //if there is are special characters, set the mode accordingly and replace them w/ whitespace
    if(foundstuff == 0){
      for(l = 0; l < strlen(token); l++){
        tmp = token[l];
        if(tmp == '|'){
          mode = 1;
          token[strcspn(token, "|")] = ' ';
          foundstuff = 1;
        }else if(tmp == ';'){
          mode = 2;
          token[strcspn(token, ";")] = ' ';
          foundstuff = 1;
        }
      }
    }
    if (foundstuff == 1){//if we found a special character, process the token accordingly. 
      int dirchange = 0;
      char wrd1[MAXCHARS];
      char wrd2[MAXCHARS];
      size_t wrd1_len = 0;
      size_t wrd2_len = 0;
      for (l = 0; l < strlen(token); l++){
        tmp = token[l];
        if (tmp == ' '){
          dirchange = 1;
        }else{
          if(dirchange == 0){
            wrd1[wrd1_len] = tmp;
            wrd1_len = wrd1_len + 1;
          }else{
            wrd2[wrd2_len] = tmp;
            wrd2_len = wrd2_len + 1; 
          }
        }
      }
      wrd1[wrd1_len] = '\0';
      wrd2[wrd2_len] = '\0';
      if(strlen(wrd1) > 0){
        cmd1[i] = wrd1;
        cmd1s = cmd1s + 1;
      }
      if(strlen(wrd2) > 0){
        cmd2[0] = wrd2;
        cmd2s = cmd2s + 1;
        i = 1;
      }else{
        i = 0;
      }
    foundstuff = 0;
    }else{//otherwise do this stuff
      if(mode == 0){
        cmd1[i] = token;
        cmd1s = cmd1s + 1;
        i = i + 1;
      }else{
        cmd2[i] = token;
        cmd2s = cmd2s + 1;
        i = i + 1;
      }
    }
    token = strtok_r(NULL, " ", &end1);
  };
  cmd1[cmd1s] = NULL;
  cmd2[cmd2s] = NULL;
  if(cmd1s == 0){
    printf("Invalid input!\n");
  }else{
    if(strcmp(cmd1[0], "exit") == 0){
      printf("Bye\n");
      exit(0);
    }else{
      execute_funct(cmd1, cmd2, mode);
    }
  } 
  return 1;
}

int main(void){
  char prompt[7] = "CS341 >";
  char *line = NULL;
  size_t linelen = 0;
  int heatDeathOfUniverse = 0;
  signal(SIGINT, handle_int);
  signal(SIGTSTP, handle_stp);
  while(heatDeathOfUniverse == 0){
    printf("%s", prompt);
    if(getline(&line, &linelen, stdin) == -1){
      printf("you blew it");
      exit(0);
    }
    line[strcspn(line, "\n")] = '\0';
    betterparseline(line);
    //printf("oo");
    if (line != NULL){
      free(line);
    }
  }
  return 0;
}