library(splines)
library(tidyverse)
library(pander)
knitr::opts_chunk$set(fig.height=3, fig.width=6, fig.align='center', warning = F, message = F)
set.seed(1)

generate_design_matrix <- function(x, knot_vector, degree){
  return(cbind(outer(x,1:degree,"^"),outer(x,knot_vector,">")*outer(x,knot_vector,"-")^degree))
}

design_matrix3 <- generate_design_matrix(degree = 1, knot_vector = seq(from = 0.1, to = 5.9, by = .2), x = x)
mod_ls3 <- lm(y~design_matrix3)
yhatbad3 <- predict(mod_ls3)
design_matrix4 <- generate_design_matrix(degree = 1, knot_vector = seq(from = 0.1, to = 5.9, by = .3), x = x)
mod_ls4 <- lm(y~design_matrix4)
yhatbad4 <- predict(mod_ls4)

ggplot() +
  geom_point(aes(x = x, y = y), color = "green", alpha = .5) +
  geom_line(aes(x = x, y = yhatbad3), color = "blue") +
  geom_line(aes(x = x, y = yhatbad4), color = "red") 