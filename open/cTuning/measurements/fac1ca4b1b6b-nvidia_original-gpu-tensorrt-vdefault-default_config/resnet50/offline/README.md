This experiment is generated using [MLCommons CM](https://github.com/mlcommons/ck)
## CM Run Command
```
cm run script \
	generate-run-cmds inference _submission _all-scenarios \
	--model=resnet50 \
	--device=cuda \
	--implementation=nvidia-original \
	--backend=tensorrt \
	--execution-mode=valid \
	--results_dir=/home/cmuser/results_dir \
	--category=edge \
	--division=open \
	--quiet \
	--skip_submission_generation=yes
```