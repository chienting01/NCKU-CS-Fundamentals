#include <stdio.h>

int main() {
    // 1. 宣告變數 (宣告箱子型態與名稱)
    int machineID = 101;        // 整數
    float temperature = 98.6;   // 小數
    char defectGrade = 'A';     // 單一字元用單引號

    // 2. 格式化輸出 (使用 %d, %f, %c 作為佔位符)
    printf("--- 生產線監控數據 ---\n");
    printf("機台編號: %d\n", machineID);      // %d 對應 int
    printf("目前溫度: %.1f\n", temperature);  // %.1f 對應 float 並取小數點後 1 位
    printf("瑕疵等級: %c\n", defectGrade);    // %c 對應 char

    return 0;
}