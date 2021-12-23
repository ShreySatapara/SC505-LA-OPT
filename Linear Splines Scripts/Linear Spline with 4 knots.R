library(splines)
library(tidyverse)
library(pander)
knitr::opts_chunk$set(fig.height=3, fig.width=6, fig.align='center', warning = F, message = F)
set.seed(1)
generate_design_matrix <- function(x, knot_vector, degree){
  return(cbind(outer(x,1:degree,"^"),outer(x,knot_vector,">")*outer(x,knot_vector,"-")^degree))
}
design_matrix2 <- generate_design_matrix(degree = 1, knot_vector = c(1,2.5,4, 5.7), x = x)
mod_ls2 <- lm(y~design_matrix2)

ggplot() +
  geom_point(aes(x = x, y = y), color = "black", alpha = .5) +
  geom_line(aes(x = x, y = predict(mod_ls2)), color = "red") +
  
  labs(title = "")