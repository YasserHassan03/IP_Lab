def ranking(smoothness_score):

	ranking_list = []

	for i in range(1, len(ranking_list)):
			ranking_list.append(smoothness_score)

	ranking_list.sort(reverse=True)

	for i in range(1, len(ranking_list)+1):
            print(f"Rank {i}: {ranking_list[i-1]}")