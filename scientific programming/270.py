with open('kegg_hsa_gmt.txt', 'r', encoding='utf-8') as f:
    table_text = f.read()

def parse_gene_paths(table_text: str) -> dict:
    gene_dict = {}
    lines = table_text.strip().split('\n')

    for line in lines:
        parts = line.split('\t')
        if len(parts) <=3:
            continue

        path_name = parts[0]
        genes = parts[2:]

        words_in_path = path_name.split('_')
        unique_words = set(words_in_path)

        for gene in genes:
            if gene not in gene_dict:
                gene_dict[gene] = {}
            
            for word in unique_words:
                gene_dict[gene][word] = gene_dict[gene].get(word,0) + 1
        
    return gene_dict

def count_paths_for_gene(
    gene_in_path: dict,
    gene: str,
    path_part: str
) -> int:
    if gene not in gene_in_path:
        return 0

    gene_data = gene_in_path[gene]
    return gene_data.get(path_part, 0)

# Пример вызова на тесте 1:
gene_in_path = parse_gene_paths(table_text)
path_count = count_paths_for_gene(
    gene_in_path, 
    'ACAA2', 
    'degradation'
)
print("path_count = ", path_count)

# Пример вызова на тесте 2:
gene_in_path = parse_gene_paths(table_text)
path_count = count_paths_for_gene(
    gene_in_path, 
    'SDS', 
    'metabolism'
)
print("path_count = ", path_count)




# более оптимизированный вариант для Python 3.8

def parse_gene_paths(table_text: str) -> dict:
    from collections import defaultdict
    gene_dict = defaultdict(lambda: defaultdict(int))

    lines = table_text.strip().split('\n')

    for line in lines:
        parts = line.split('\t')
        if len(parts) < 3:
            continue

        path_name = parts[0]
        genes = parts[2:]

        words_in_path = set(path_name.split('_'))

        for gene in genes:
            if gene:
                for word in words_in_path:
                    gene_dict[gene][word] += 1

    return gene_dict


def count_paths_for_gene(
    gene_in_path: dict, 
    gene: str, 
    path_part: str
) -> int:
    if gene not in gene_in_path:
        return 0
    return gene_in_path[gene].get(path_part, 0)
