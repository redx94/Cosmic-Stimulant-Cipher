import numpy as np
from Bio.Seq import Seq
from Bio import motifs
from itertools import product

class DNAKeyExpander:
    def __init__(self):
        self.nucleotides = ['A', 'T', 'G', 'C']
        self.codon_map = self._create_codon_map()
        
    def _create_codon_map(self):
        """Create mapping between hex digits and DNA codons"""
        codons = [''.join(p) for p in product(self.nucleotides, repeat=3)]
        hex_digits = '0123456789abcdef'
        return dict(zip(hex_digits, codons[:16]))
        
    def hex_to_dna(self, hex_key):
        """Convert hex key to DNA sequence"""
        return ''.join(self.codon_map[d] for d in hex_key.lower())
        
    def simulate_transcription(self, dna_seq):
        """Simulate DNA transcription process"""
        seq = Seq(dna_seq)
        rna = seq.transcribe()
        return str(rna)
        
    def simulate_mutation(self, dna_seq, mutation_rate=0.01):
        """Simulate genetic mutation"""
        dna_list = list(dna_seq)
        for i in range(len(dna_list)):
            if np.random.random() < mutation_rate:
                dna_list[i] = np.random.choice(self.nucleotides)
        return ''.join(dna_list)
        
    def find_motifs(self, dna_seq):
        """Find recurring patterns in DNA sequence"""
        instances = []
        for i in range(0, len(dna_seq)-6, 3):
            instances.append(Seq(dna_seq[i:i+6]))
        m = motifs.create(instances)
        return m.consensus
        
    def expand_key(self, hex_key, rounds=3):
        """Expand key using DNA-inspired processes"""
        dna = self.hex_to_dna(hex_key)
        expanded = dna
        
        for _ in range(rounds):
            rna = self.simulate_transcription(expanded)
            mutated = self.simulate_mutation(rna)
            motif = self.find_motifs(mutated)
            expanded += str(motif)
            
        return hashlib.sha3_512(expanded.encode()).hexdigest()
