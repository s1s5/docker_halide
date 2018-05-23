# halide executable

## USAGE
### docker image の取得
``` shell
$ docker pull --disable-content-trust s1s5/halide
```

### runtimeライブラリの出力
`$ docker run -i --rm s1s5/halide runtime x86-64 > /tmp/halide_runtime.a`

x86-64のところには`target`が入る（後述）


### header, objの出力
``` shell
docker run -i -e CXX_FLAGS="-std=c++1z" --rm -v `pwd`/examples:/work s1s5/halide h copy.cpp -g copy -f hoge_copy target=x86-64-no_runtime > /tmp/copy.h

docker run -i -e CXX_FLAGS="-std=c++1z" --rm -v `pwd`/examples:/work s1s5/halide h src/mod/copy.cpp -g copy -f hoge_copy target=x86-64-no_runtime > /tmp/copy.h
docker run -i -e CXX_FLAGS="-std=c++1z" --rm -v `pwd`/examples:/work s1s5/halide o src/mod/copy.cpp -g copy -f hoge_copy target=x86-64-no_runtime > /tmp/copy.o
```

かならず/workにマウントして、ソースファイルは相対パスで記述する。
第一引数は、h, oのどちらか。それぞれ、ヘッダファイル、オブジェクトファイルを出力する

以下のオプションが必須
<dl>
  <dt>-g</dt>
  <dd>generatorの名前。HALIDE_REGISTER_GENERATOR(CopyGenerator, <generator name>)で指定したやつ。</dd>
  <dt>-f</dt>
  <dd>出力される関数名</dd>
  <dt>target=**</dt>
  <dd>出力するターゲットを指定する（後述）</dd>
</dl>


# halideで指定するターゲットについて
## フォーマット
- `arch-bits-os-feature1-feature2-...`

以下のパターンがあるみたいなので、適当に組み合わせる。
no_runtimeをつけるとruntimeライブラリを同時に出力しなくなる

## arch
- x86
- arm
- arch_unknown
- hexagon
- mips
- powerpc

## bits
- 32
- 64

## os
- android
- ios
- linux
- noos
- os_unknown
- osx
- qurt
- windows

## feature
- armv7s
- avx
- avx2
- avx512
- avx512_cannonlake
- avx512_knl
- avx512_skylake
- c_plus_plus_name_mangling
- cl_doubles
- cl_half
- cuda
- cuda_capability_30
- cuda_capability_32
- cuda_capability_35
- cuda_capability_50
- cuda_capability_61
- debug
- f16c
- fma
- fma4
- fuzz_float_stores
- hvx_128
- hvx_64
- hvx_shared_object
- hvx_v62
- hvx_v65
- hvx_v66
- jit
- large_buffers
- matlab
- metal
- mingw
- msan
- no_asserts
- no_bounds_query
- no_neon
- no_runtime
- opencl
- opengl
- openglcompute
- power_arch_2_07
- profile
- soft_float_abi
- sse41
- trace_loads
- trace_realizations
- trace_stores
- user_context
- vsx

## サンプル
- `x86-64-linux-avx-avx2-f16c-fma-sse41`
- `x86-64`
- `ios-arm-64-opengl`
- `x86-64-no_runtime`
