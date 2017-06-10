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

## sort and rank 
sortindex<- order(DF[,2])
rnk<-rank(DF[,2])

## handles big df better
temp<-as.tibble(cbind(rnk, DF[,2]))

## aesthetics 
colnames(temp)<-c("rank", "count")

temp$count<-log(temp$count+1)

## scale rank 
temp$rank<-temp$rank/nrow(temp)

## save plot
p<- qplot(temp$rank, temp$count, xlab="rank", ylab="log(count)", main=args[2])

## set filename 
file<-paste(args[2], ".png", sep="")

## save plot 
ggsave(file, plot=p, device="png")
  
