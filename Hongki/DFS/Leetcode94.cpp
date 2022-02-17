/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    
void dfs(vector<int>& store, TreeNode* root) {
    if (!root) return;
       dfs(store, root->left);
       store.push_back(root->val);
       dfs(store, root->right);
}
    
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> store;
        dfs(store, root);
        return store;
    }

};
