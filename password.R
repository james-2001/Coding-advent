library('stringr')

data=read.delim("passwords2.txt")
numbs<-split(unlist(strsplit(data$X4.8,"-")),1:2)
numframe<-data.frame(x=numbs$"1",y=numbs$"2")
letters<-data$g
passwords<-data$ggtxgtgbg

check <- function(i){
  lower=strtoi(unlist(numframe[i,1]))
  upper=strtoi(unlist(numframe[i,2]))
  letter=letters[i]
  pword=passwords[i]
  val=str_count(pword,letter)
  if((val>=lower)&(val<=upper)){
    return(1)
  }
  else{return(0)}
}

v=sapply(1:length(letters),FUN=check)
print(sum(v)+1) #+1 as first password read as a title

check2 <-function(i){
  lower=strtoi(unlist(numframe[i,1]))
  upper=strtoi(unlist(numframe[i,2]))
  letter=letters[i]
  password=unlist(strsplit(passwords[i],split = ""))
  ret<-0
  if((password[lower]==letter)|(password[upper]==letter)){ret<-1}
  if((password[lower]==letter)&(password[upper]==letter)){ret<-0}
  return(ret)
}

v2=sapply(1:length(letters),FUN=check2)
print(sum(v2)+1)


