class TwoPairs {
    boolean hasArrayTwoCandidates(int arr[], int x) {
        // code here
        int len = arr.length;
        for (int i = 0; i < len; i++) {
            for (int j = i+1; j < len; j++) {
                if (arr[i] + arr[j] == x) {
                    return true;
                }
            }
        }
        return false;
    }
}