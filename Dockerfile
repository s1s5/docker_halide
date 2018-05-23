# -*- mode: dockerfile -*-
from halide-base

MAINTAINER Shogo Sawai

ADD halide /opt/source/halide
RUN mkdir /opt/build/halide
WORKDIR /opt/build/halide
RUN cmake -DLLVM_DIR=/usr/lib/cmake/llvm/ -DCMAKE_BUILD_TYPE=Release /opt/source/halide
RUN make -j8

WORKDIR /

RUN cp /opt/build/halide/bin/halide_library_runtime.generator_binary /usr/local/bin/

RUN cp -r /opt/build/halide/include /usr/include/halide
RUN cp /opt/build/halide/lib/libHalide.so /usr/lib

RUN mkdir /work
RUN mkdir /build
RUN mkdir /halide
WORKDIR /build

ADD entrypoint.py /opt/
ENTRYPOINT ["python", "/opt/entrypoint.py"]
