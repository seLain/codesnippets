import java.util.*;

public class UniqueCharsCheck {

	public boolean check(String words){
		char[] chars = words.toCharArray();
		Set<Character> set = new HashSet<Character>();
		for(char c : chars){
			if(set.contains(c)){
				return false;
			}else{
				set.add(c);
			}
		}
		return true;
	}

	public static void main(String args[]){
		UniqueCharsCheck checker = new UniqueCharsCheck();
		System.out.println(checker.check("Unique")?"Yes":"No");
		System.out.println(checker.check("UniqUe")?"Yes":"No");
	}

}