#


install.packages("curl")
install.packages("httr")
install.packages("devtools")
install.packages("reticulate")

library("devtools")
devtools::install_github("rstudio/keras")

library("keras")
install_keras()
