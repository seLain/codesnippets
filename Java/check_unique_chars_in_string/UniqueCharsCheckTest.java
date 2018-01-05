import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class UniqueCharsCheckTest {
  @Test
  public void evaluatesExpression() {
    UniqueCharsCheck uchecker = new UniqueCharsCheck();
    boolean result = false;
    result = uchecker.check("Unique");
    assertEquals(result, true);
    result = uchecker.check("UniqUe");
    assertEquals(result, false);
  }
}