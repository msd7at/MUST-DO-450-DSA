#https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1#
    def isValid(self, s: str) -> bool:
        st=[]
        va={"(",'[','{'}
        av={")",']','}'}
        for i in s:
            if i in va:
                st.append(i)
            else:
                if st==[]:
                    return False
                if i==")" :
                    if st[-1]=="(":
                        st.pop()
                    else:
                        return False
                elif i=="]" :
                    if st[-1]=="[":
                        st.pop()
                    else:
                        return False
                elif i=="}":
                    if st[-1]=="{":
                        st.pop()
                    else:
                        return False  
        if st==[]:
            return True
        return False
