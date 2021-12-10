library(splines)
library(tidyverse)
library(pander)
knitr::opts_chunk$set(fig.height=3, fig.width=6, fig.align='center', warning = F, message = F)
set.seed(1)

knot <- 3 # This is the location of our (in this case single) knot
x <- seq(from = 0, to = 6, by = .025)
y <- sin(2*x) + x -.1*x^2 + 2 + rnorm(length(x), sd = .3)

# More on this design matrix later...
design_matrix_X <- cbind(outer(x,1:1,"^"),outer(x,knot,">") * outer(x,knot,"-")^1)

mod_ls <- lm(y~design_matrix_X)
ggplot() +
  geom_point(aes(x = x, y = y), color = "green", alpha = .5) +
  geom_line(aes(x = x, y = predict(mod_ls)), color = "red") +
  geom_vline(aes(xintercept = knot), alpha = .5, linetype = "dotdash") +
  labs(title = "")
