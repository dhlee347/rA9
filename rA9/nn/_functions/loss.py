import jax.numpy as jnp
from rA9.autograd import Function
from rA9.autograd import Variable


class Spikeloss(Function):
    id = "Spikeloss"

    @staticmethod
    def forward(ctx, input, target, time_step):
        assert isinstance(input, Variable)
        assert isinstance(target, Variable)

        def np_fn(input_np, target_np, time_step):
            return jnp.sum((input_np - jnp.tile(jnp.expand_dims(target_np, axis=1), target_np.shape[1:])) ** 2) / 2

        np_args = (input.data, target.data, time_step)
        id = "Spikeloss"

        return np_fn, np_args, np_fn(*np_args), id

    @staticmethod
    def backward(ctx, grad_outputs):
        return super(Spikeloss, Spikeloss).backward(ctx, grad_outputs)
