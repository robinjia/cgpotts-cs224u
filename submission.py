from distributedwordreps import *

def wordword_pmi_svd(ww, k=100):
  ww_ppmi = pmi(mat=ww[0], rownames=ww[1], positive=True)
  return lsa(ww_ppmi[0], ww_ppmi[1], k=k)


def worddoc_pmi_svd(wd, k=100):
  wd_ppmi = pmi(mat=wd[0], rownames=wd[1], positive=True)
  return lsa(wd_ppmi[0], wd_ppmi[1], k=k)


def get_score(x):
  return word_similarity_evaluation(mat=x[0], rownames=x[1])



def main():
  print >> sys.stderr, 'Reading word-word matrix'
  ww = build('distributedwordreps-data/imdb-wordword.csv')
  # print >> sys.stderr, 'Reading word-document matrix'
  # wd = build('distributedwordreps-data/imdb-worddoc.csv')
  ww_vecs = wordword_pmi_svd(ww)

  score = word_similarity_evaluation(mat=ww_vecs[0], rownames=ww_vecs[1])

if  __name__ == '__main__':
  main()
