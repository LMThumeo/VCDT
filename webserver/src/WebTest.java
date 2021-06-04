import static org.junit.Assert.assertEquals;
import org.junit.Test;
public class WebTest {   
    
    @Test
    public void webServerPortTest()  {
        int expectedPort = 6789;
        WebServer webServer = new WebServer();
        int actualPort = webServer.getPort();
        assertEquals(expectedPort, actualPort);     
    }    
}
