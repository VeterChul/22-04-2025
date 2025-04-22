def tree(chars  : dict) -> dict:
  if len(chars) == 1:
    for i in chars:
      return {i : ""}
  sort_ch = sort(chars.copy(), True)
  n = chars[sort_ch[0]] + chars[sort_ch[1]]

  del chars[sort_ch[0]]
  del chars[sort_ch[1]]

  chars[sort_ch[0] + sort_ch[1]] = n
  codes = tree(chars)
  res = codes[sort_ch[0] + sort_ch[1]]
  del codes[sort_ch[0] + sort_ch[1]]
  codes[sort_ch[0]] = res +"0"
  codes[sort_ch[1]] = res +"1"
  return codes

def sort(chars : dict, f : bool) -> list:
  max = 0
  for i in chars:
    if max <= chars[i]:
      max = chars[i]
      i_max = i
  min = max
  i_min = i_max
  for i in chars:
    if min > chars[i]:
      min = chars[i]
      i_min = i

  if f:
    del chars[i_min]
    return [i_min, sort(chars ,False)]
  return i_min

