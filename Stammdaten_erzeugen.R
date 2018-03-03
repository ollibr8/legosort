# Stammdaten definieren

library(magrittr)

setwd("~/Dokumente/Legosortiermaschine")

length <- c(1:12)
width <- c(1,2) %>% as.integer()
col <- c("black", "green", "red", "yellow", "blue", "white") %>% as.factor()
height <- c(1,3) %>% as.integer()

stammdaten <- expand.grid(length = length, 
                          width = width, 
                          col = col, 
                          height = height)

stammdaten$ID <- 1:nrow(stammdaten)

stammdaten <- stammdaten[,c("ID", "length", "width", "col", "height")]

write.csv2(stammdaten, "Stammdaten.csv")
           
