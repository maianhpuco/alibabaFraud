# Fraud Detection - Alibaba 
This repo is to practise some code implementing from this paper
Please read through the paper before continue: 
https://nesa.zju.edu.cn/download/Online%20E-Commerce%20Fraud%20A%20Large-scale%20Detection%20and%20Analysis.pdf


## Introduction: 
This repo is only for practising purpose so: 
- it does not have high credibility
- performance of code may be (or will) not good, so all feedback and comment are highly welcome 


## About the paper (quick summary, quoting from paper) 
There are 2 modules in this paper: 
- GBD module (Graph-Based Detection module): this module using an "user-item bipartite graph and a small set of confirmed dishonest users, GBD assigns each item a fraud score via a propagation algorithm. Then, it determines the fraud items based on their fraud scores."  - page 2 
- TSD module (Time Series based Detection module): " TSD is designed based on the observation that when a new fraud pattern appears or a new item becomes a fraud item, the traffic time series of the new fraud item is likely to exhibit differently from the benign items. Therefore, it first makes a hypothesis that the traffic time series of each item follows a mixture Poissondistribution. Then, it derives an abnormal score for the traffic time series of each item, and determines the fraud items based on the abnormal scores."  - page 2 



