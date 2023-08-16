This experiment is generated using [MLCommons CM](https://github.com/mlcommons/ck)
## CM Run Command
```
cm run script \
	generate-run-cmds inference _populate-readme \
	--implementation=nvidia-original \
	--device=cuda \
	--backend=tensorrt \
	--category=edge \
	--division=open \
	--quiet \
	--execution_mode=valid \
	--preprocess_submission \
	--results_dir=/home/cmuser/results_dir \
	--scenario=Offline \
	--offline_target_qps=4 \
	--gpu_name=rtx_4090 \
	--power=yes \
	--adr.mlperf-power-client.power_server=192.168.0.15 \
	--model=3d-unet-99
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


9. `cm run script --tags=get,mlcommons,inference,src`


10. `cm run script --tags=get,nvidia,mlperf,inference,common-code,_nvidia-only`


11. `cm run script --tags=generate,user-conf,mlperf,inference`


12. `cm run script --tags=get,generic-python-lib,_transformers`


13. `cm run script --tags=reproduce,mlperf,inference,nvidia,harness,_build_engine,_batch_size.8,_cuda,_3d-unet-99,_tensorrt,_offline,_rtx_4090,_3d-unet_`


14. `cm run script --tags=reproduce,mlperf,inference,nvidia,harness,_preprocess_data,_cuda,_3d-unet-99,_tensorrt,_rtx_4090,_3d-unet_`


15. `cm run script --tags=reproduce,mlperf,inference,nvidia,harness,_download_model,_cuda,_3d-unet-99,_tensorrt,_rtx_4090,_3d-unet_`
