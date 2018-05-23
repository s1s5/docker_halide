# halide executable

## USAGE

``` shell
$ docker pull --disable-content-trust s1s5/halide
```

### 
Expected format is arch-bits-os-feature1-feature2-...
Where arch is: arch_unknown, arm, hexagon, mips, powerpc, x86.
bits is either 32 or 64.
os is: android, ios, linux, noos, os_unknown, osx, qurt, windows.

If arch, bits, or os are omitted, they default to the host.

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

sets the host's architecture, os, and feature set

`x86-64-linux-avx-avx2-f16c-fma-sse41`

x86-64
ios-arm-64-opengl


``` shell
$ docker run -i --rm s1s5/halide runtime x86-64 > /tmp/halide_runtime.a


$ docker run -i --rm -v `pwd`/examples:/work s1s5/halide h rgb2gray.cpp > /tmp/rgb2gray.h

```

docker run -i -e CXX_FLAGS="-std=c++1z" --rm -v `pwd`/examples:/work s1s5/halide h copy.cpp -g copy -f hoge_copy target=x86-64-no_runtime > /tmp/copy.h

docker run -i -e CXX_FLAGS="-std=c++1z" --rm -v `pwd`/examples:/work s1s5/halide h src/mod/copy.cpp -g copy -f hoge_copy target=x86-64-no_runtime > /tmp/copy.h
docker run -i -e CXX_FLAGS="-std=c++1z" --rm -v `pwd`/examples:/work s1s5/halide o src/mod/copy.cpp -g copy -f hoge_copy target=x86-64-no_runtime > /tmp/copy.o
