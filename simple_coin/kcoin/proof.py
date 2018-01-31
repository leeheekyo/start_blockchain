import hashlib

import kcoin.config as cfg


def valid_proof(block, proof=None):
    # block : obj
    # proof : int
    proof = proof if proof else block.proof

    proof_seed = '{0}{1}'.format(block.header.hash(),
                                 proof).encode()

    proof_hash = hashlib.sha256(proof_seed).hexdigest()

    return proof_hash[:block.difficulty] == cfg.PROOF_DIGITS * block.difficulty


def find_proof(block):
    # block : obj
    proof = 0

    while valid_proof(block, proof) is False:
        proof += 1

    return proof

