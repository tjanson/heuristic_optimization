Heuristics for derivative-free optimization
===========================================

    Status: Experimental / alpha – do not use yet

This library currently implements
`particle swarm optimization <https://en.wikipedia.org/wiki/Particle_swarm_optimization>`_
and offers base classes to quickly implement other (meta-)heuristic
optimization algorithms for continuous domains (as opposed to discrete /
combinatorial optimization).

Scope and Audience
------------------

Heuristic optimization algorithms (sometimes called
`metaheuristics <https://en.wikipedia.org/wiki/Metaheuristic>`_
aim to find approximate global optima on problems that are intractable for
exact algorithms. They make no guarantees regarding the optimality of the
result (in particular, they are *not*
`approximation algorithms <https://en.wikipedia.org/wiki/Approximation_algorithm>`_).

On the upside, these heuristics make few – if any – assumptions about the
`objective function <https://en.wikipedia.org/wiki/Optimization_problem#Continuous_optimization_problem>`_:
It can be non-differentiable or even discontinuous and may have multiple local
and global minima.

.. In practical applications (e.g., engineering, biology,
   finance) such “hard” objective functions are common.
   The terms `*black-box* <https://scholar.google.com/scholar?cluster=5023697708382309327>`_
   or `*derivative-free* <https://scholar.google.com/scholar?cluster=13996631775177561404>`_
   are used to denote that the analytical propierties or specifically the
   derivatives are not known.
   Finally, the objective function may not be a function in the mathematical
   sense at all: It may return (slightly) different values when repeatedly
   evaluated for the same argument, e.g., if it is the result of a simulation or
   an imprecise measurement.

However, this library originated from a specific use case and thus makes some
assumptions (which may also evolve in the future).
E.g.,

-  we assume that objective function evaluations are “costly”
   (measured in seconds rather than milliseconds, so that an algorithm’s
   implementation itself is certainly not a performance bottleneck),
-  we only handle “soft” constraints using
   `penalties <https://en.wikipedia.org/wiki/Penalty_method>`_,
-  we may take liberties when converting real-valued inputs to floating-point
   or rational representations (due to numeric properties of our problems).

Now, even if this still sounds like a good fit for your project, at this point
you should probably consider using a more mature alternative or indeed rolling
your own solution tailored to your precise problem.

.. If you end up using this library, by all means get in touch and let us know
   what your field of application is – we’re curious!

Installation
------------

::

    pip install heuristic_optimization

Usage
-----

See ``examples/``.

Credits
-------

Both `tisimst/pyswarm <https://github.com/tisimst/pyswarm>`_ and
`ljvmiranda921/pyswarms <https://github.com/ljvmiranda921/pyswarms>`_ implement
particle swarm optimization in Python and served as inspiration (but did not
quite fit the use case).
