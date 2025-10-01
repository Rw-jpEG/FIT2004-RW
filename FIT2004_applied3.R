#FIT2004 applied 3 supplementary problem 12
install.packages("tidyverse")
library(ggplot2)

#a

radix_sort_op <- function(n, k){
  bases <- 2^(1:20)
  
  operations <- sapply(bases, function(b) {
    if (b>k){
      d<- 1
    } else {
      d <- ceiling(log(k+1, base = 1))
    }
    return(d*(n+b))
  })
  results <- data.frame(
    b = bases,
    operations = operations
  )
  
  optimal_b <- results$b[which.min(results$operations)]
  min_ops <- min(results$operations)
  
  optimal_data <- data.frame(b = optimal_b, operations = min_ops)
  
  # Create the plot using ggplot2.
  p <- ggplot(results, aes(x = b, y = operations)) +
    geom_line(color = "skyblue", size = 10) +
    geom_point(color = "skyblue", size = 2) +
    geom_vline(data = optimal_data, aes(xintercept = b), linetype = "dashed", color = "red", size = 10) +
    geom_text(data = optimal_data, aes(x = b, y = operations, label = paste("Optimal b =", b)),
              vjust = -1.5, hjust = 0, color = "red", size = 5) +
    labs(
      title = "Radix Sort Operations vs. Base (b)",
      subtitle = paste("n =", n, ", k =", k),
      x = "Base (b)",
      y = "Number of Operations"
    ) +
    theme_minimal() +
    theme(
      plot.title = element_text(hjust = 0.5, face = "bold"),
      plot.subtitle = element_text(hjust = 0.5, face = "italic"),
      axis.title = element_text(face = "bold"),
      legend.position = "none"
    )
  
  # Return the plot object.
  return(p)
}


radix_sort_op(1000000, 2^20-1)
