class Solution:
    def accountsMerge(self, accounts):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}

        # 初始化 parent 并记录邮箱对应的人名
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

            # 同一账户内的邮箱都合并
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        # 根据 root 分组
        from collections import defaultdict
        unions = defaultdict(list)
        for email in parent:
            root = find(email)
            unions[root].append(email)

        # 构造结果
        res = []
        for root, emails in unions.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))

        return res

# 测试
if __name__ == "__main__":
    solution = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"]
    ]
    merged_accounts = solution.accountsMerge(accounts)
    for account in merged_accounts:
        print(account)