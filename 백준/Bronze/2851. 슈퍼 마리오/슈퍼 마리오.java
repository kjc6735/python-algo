
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Main {
    static int []arr = new int[10];

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i = 0; i < 10; i++) arr[i] = Integer.parseInt(br.readLine());
        int max = 0;
        int tmp = 0;
        for(int i = 0; i < 10; i++) {
            tmp += arr[i];
            int curr = Math.abs(100 - tmp);
            int maxCurr = Math.abs(100 - max);
            if(curr < maxCurr ){
                max = tmp;
            }else if(curr == maxCurr){
                max = Math.max(tmp, max);
            }
        }
        System.out.println(max);
    }
}
