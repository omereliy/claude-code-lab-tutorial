(define (domain blocksworld)
  (:requirements :strips :typing)

  ; NOTE: 'crate' is intentionally NOT declared here — see action `stack`.
  (:types block - object)

  (:predicates
    (on ?x - block ?y - block)
    (ontable ?x - block)
    (clear ?x - block)
    (holding ?x - block)
    (handempty))

  (:action pick-up
    :parameters (?x - block)
    :precondition (and (clear ?x) (ontable ?x) (handempty))
    :effect (and (not (ontable ?x)) (not (clear ?x))
                 (not (handempty)) (holding ?x)))

  (:action put-down
    :parameters (?x - block)
    :precondition (holding ?x)
    :effect (and (not (holding ?x)) (clear ?x) (handempty) (ontable ?x)))

  ; This action has three planted errors:
  ;   - parameter ?y uses undeclared type 'crate'
  ;   - precondition uses undeclared predicate 'stackable'
  ;   - effect uses 'on' with 3 args, but it is declared with arity 2
  (:action stack
    :parameters (?x - block ?y - crate)
    :precondition (and (holding ?x) (clear ?y) (stackable ?y))
    :effect (and (not (holding ?x)) (not (clear ?y))
                 (clear ?x) (handempty) (on ?x ?y ?y)))
)
