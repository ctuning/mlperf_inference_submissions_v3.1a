This experiment is generated using [MLCommons CM](https://github.com/mlcommons/ck)
## CM Run Command
```
cm run script \
	run mobilenet-models _tflite _armnn _neon _accuracy-only \
	--adr.compiler.tags=gcc \
	--results_dir=/home/arjun/mobilenet_results \
	--power1=yes \
	--adr.mlperf-power-client.power_server=192.168.0.15 \
	--adr.mlperf-power-client.port=4940 \
	--adr.armnn.version=22.11
```