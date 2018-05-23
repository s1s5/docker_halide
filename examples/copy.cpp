/**
 * Copyright 2015- Co. Ltd. sizebook
 * @file copy.cpp
 * @brief
 * @author Shogo Sawai
 * @date 2018-05-23 10:39:37
 */

#include "halide/Halide.h"

using namespace Halide;

class CopyGenerator : public Generator<CopyGenerator> {
 public:
    // command lineで"-t"で指定可能？
    Input<Buffer<uint8_t>> input{
        "input",
        3,
    };
    Output<Buffer<uint8_t>> output{
        "output",
        3,
    };

    Var x, y, c;

    void generate() {
        output(x, y, c) = input(x, y, c);
    }

    void schedule() {
        input.dim(0).set_stride(Expr());
        output.dim(0).set_stride(Expr());

        Expr input_is_planar = (input.dim(0).stride() == 1);
        Expr input_is_interleaved =
            (input.dim(0).stride() == 3 && input.dim(2).stride() == 1 && input.dim(2).extent() == 3);

        Expr output_is_planar = (output.dim(0).stride() == 1);
        Expr output_is_interleaved =
            (output.dim(0).stride() == 3 && output.dim(2).stride() == 1 && output.dim(2).extent() == 3);

        output.specialize(input_is_planar && output_is_planar);
        output.specialize(input_is_interleaved && output_is_interleaved).reorder(c, x, y).unroll(c);
    }
};

HALIDE_REGISTER_GENERATOR(CopyGenerator, copy)

int main(int argc, char **argv) {
    return Halide::Internal::generate_filter_main(argc, argv, std::cerr);
}

