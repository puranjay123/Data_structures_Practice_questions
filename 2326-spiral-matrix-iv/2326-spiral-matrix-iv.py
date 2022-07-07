class Solution:
    def spiralMatrix(self, rows: int, cols: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * cols for _ in range(rows)]
        rows1, cols1 = rows - 1, cols - 1
        min_layers = min(rows, cols) // 2
        for i in range(min_layers):
            for c in range(i, cols1 - i):
                ans[i][c] = head.val
                head = head.next
                if not head:
                    return ans
            col = cols1 - i
            for r in range(i, rows1 - i):
                ans[r][col] = head.val
                head = head.next
                if not head:
                    return ans
            row = rows1 - i
            for c in range(cols1 - i, i, -1):
                ans[row][c] = head.val
                head = head.next
                if not head:
                    return ans
            for r in range(rows1 - i, i, -1):
                ans[r][i] = head.val
                head = head.next
                if not head:
                    return ans
        if rows <= cols and rows % 2:
            for c in range(min_layers, cols - min_layers):
                ans[min_layers][c] = head.val
                head = head.next
                if not head:
                    return ans
        elif cols % 2:
            for r in range(min_layers, rows - min_layers):
                ans[r][min_layers] = head.val
                head = head.next
                if not head:
                    return ans
        return ans