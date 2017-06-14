#!/usr/bin/env Rscript

## load required libraries 
library(ggplot2)

library(tibble)

## get cmd line arguments 
args = commandArgs(trailingOnly=TRUE)

# args[1] is infile name 
# args[2] is base outfile name

## read in table 
DF<-read.table(args[1], header=T)

## sort from high to low 
DF<-DF[order(DF[,2], decreasing=TRUE),]

## rank from high to low 
rnk<-rank(-DF[,2], ties.method="first")

temp<-as.tibble(cbind(rnk, DF[,2]))

## aesthetics 
colnames(temp)<-c("rank", "count")

## scale rank 
temp$rank<-temp$rank/nrow(temp)

## cumulative sums
temp[,2]<-cumsum(temp[,2])

## count on log scale
#temp$count<-log(temp$count+1)

## save plot
# for log
#p<- qplot(temp$rank, temp$count, xlab="rank", ylab="log(count cum. sum)", ylim=c(6,20), main=args[2])

# non- log
p<- qplot(temp$rank, temp$count, xlab="rank", ylab="count cum. sum", main=args[2])

## set filename 
file<-paste(args[2], ".png", sep="")

## save plot 
ggsave(file, plot=p, device="png")
  
