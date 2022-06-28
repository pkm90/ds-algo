class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        
        # add products to a trie
        # iterate through searchword
        # for each character, add it to a prefix and grab all words after prefix from trie
        # sort the results and grab the first 3 words, append to res
        

        
        def removeProducts(prods, pref):
            resProds = prods.copy()
            for pdx, p in enumerate(prods):
                for idx, c in enumerate(pref):
                    if idx >= len(p) or p[idx] != c:
                        resProds.remove(p)
                        break
            return resProds
        
                
        res = []
        pref = ""
        
        # alternatively, we can simply sort the products
        products.sort()
        
        # iterate through searchword
        for char in searchWord:
            pref += char
            
            # if any character doesn't have the same prefix, then remove from products
            products = removeProducts(products, pref)
            
            # grab first 3 words and append to res
            res.append(products[:3])
                        
        return res