data=read.delim("passwords2.txt")
numbs<-split(unlist(strsplit(data$X4.8,"-")),1:2)
numframe<-data.frame(x=numbs$"1",y=numbs$"2")
print(numframe)
letters<-data$g
print(letters)
passwords<-data$ggtxgtgbg

check <- function(i){
  lower=unlist(numframe[i,1])
  upper=unlist(numframe[i,2])
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



