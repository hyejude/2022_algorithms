package PL1;
// �迭{}�� �Ű������� �����Ϸ��� �����ϰ� (����) �����ؾ� �Ѵٴ� �� python�̶� �ٸ��� ����.

public class Avg {
	public double solution(int[] arr){
		double sum = 0;
		for(int i=0;i<arr.length;i++){
			sum += arr[i];
		}
		return sum/arr.length;
	}
	public static void main(String[] args){
		Avg avg = new Avg();
		int[] test_arr01 = {1,2,3,4};
		int[] test_arr02 = {5,5};
		System.out.println(avg.solution(test_arr02));
	}
}
