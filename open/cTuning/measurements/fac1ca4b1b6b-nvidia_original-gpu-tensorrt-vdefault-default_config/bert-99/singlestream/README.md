This experiment is generated using [MLCommons CM](https://github.com/mlcommons/ck)
## CM Run Command
```
cm run script \
	generate-run-cmds inference _performance-only \
	--model=bert-99 \
	--implementation=nvidia-original \
	--device=cuda \
	--backend=tensorrt \
	--category=edge \
	--division=open \
	--quiet \
	--scenario=SingleStream \
	--env.CM_MLPERF_USE_MAX_DURATION=no \
	--rerun \
	--singlestream_target_latency=7.5 \
	--execution-mode=valid \
	--results_dir=/home/cmuser/results_dir
```