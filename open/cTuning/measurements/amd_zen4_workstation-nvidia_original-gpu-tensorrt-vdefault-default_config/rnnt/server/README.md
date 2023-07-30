This experiment is generated using [MLCommons CM](https://github.com/mlcommons/ck)
## CM Run Command
```
cm run script \
	generate-run-cmds inference _populate-readme _all-scenarios \
	--implementation=nvidia-original \
	--device=cuda \
	--backend=tensorrt \
	--quiet \
	--execution_mode=valid \
	--preprocess_submission \
	--results_dir=/home/cmuser/results_dir \
	--gpu_name=rtx_4090 \
	--power=yes \
	--adr.mlperf-power-client.power_server=192.168.0.15 \
	--division=open \
	--model=rnnt \
	--offline_target_qps=38000 \
	--singlestream_target_latency=0.23 \
	--multistream_target_latency=0.4 \
	--server_target_qps=14150 \
	--category=datacenter
```
## Dependent CM scripts 


1.  `cm run script --tags=detect,os`


2.  `cm run script --tags=get,sys-utils-cm`


3.  `cm run script --tags=get,python`


4.  `cm run script --tags=get,mlcommons,inference,src`

## Dependent CM scripts for the MLPerf Inference Implementation


1. `cm run script --tags=detect,os`


2. `cm run script --tags=detect,cpu`


3. `cm run script --tags=get,sys-utils-cm`


4. `cm run script --tags=get,cuda,_cudnn`


5. `cm run script --tags=get,tensorrt`


6. `cm run script --tags=build,nvidia,inference,server,_nvidia-only`


7. `cm run script --tags=get,mlperf,inference,nvidia,scratch,space`


8. `cm run script --tags=get,generic-python-lib,_mlperf_logging`


9. `cm run script --tags=get,dataset,original,librispeech`


10. `cm run script --tags=get,mlcommons,inference,src`


11. `cm run script --tags=get,nvidia,mlperf,inference,common-code,_nvidia-only`


12. `cm run script --tags=generate,user-conf,mlperf,inference`


13. `cm run script --tags=get,generic-python-lib,_toml`


14. `cm run script --tags=get,generic-python-lib,_torchvision`


15. `cm run script --tags=get,generic-python-lib,_torch`


16. `cm run script --tags=get,generic-python-lib,_nvidia-apex`


17. `cm run script --tags=get,generic-python-lib,_unidecode`


18. `cm run script --tags=get,generic-python-lib,_inflect`


19. `cm run script --tags=get,generic-python-lib,_librosa`


20. `cm run script --tags=get,generic-python-lib,_sox`


21. `cm run script --tags=get,generic-sys-util,_sox`


22. `cm run script --tags=reproduce,mlperf,inference,nvidia,harness,_build_engine,_batch_size.2048,_tensorrt,_cuda,_server,_rnnt,_rtx_4090`


23. `cm run script --tags=reproduce,mlperf,inference,nvidia,harness,_preprocess_data,_tensorrt,_cuda,_rnnt,_rtx_4090`


24. `cm run script --tags=reproduce,mlperf,inference,nvidia,harness,_download_model,_tensorrt,_cuda,_rnnt,_rtx_4090`
