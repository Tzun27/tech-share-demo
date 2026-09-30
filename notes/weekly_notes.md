weekly notes (rough, for thursday group meeting)

- ran 30 finetune runs on sst-3 this week. 4 models (bert-base-uncased, roberta-base, distilbert-base-uncased, deberta-v3-small), lr from 1e-5 to 5e-5
- 21 finish ok, 4 die with cuda OOM (2 distilbert, 2 roberta), 5 stopped because loss go nan
- best run is bert-base-uncased with lr 2e-5, val acc 0.930. bert is also best on average, 0.862 mean over its 4 finished runs
- roberta is worst on average (0.746), weird, i expected it better than bert. maybe lr too low or my tokenizer setting wrong, need check
- found a bug in eval script: macro-F1 crash when a class is never predicted. fixed, now gives 0 for that class
- after fix: macro-F1 is 0.534 on current predictions. neutral f1 is 0.000 -> model never predict neutral!!
- next week: check roberta tokenizer, rerun the nan runs with gradient clipping, try class weights for neutral
