import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class WebServer {

    int port;
    
    public WebServer() {
        port=6789;       
    }
    public int getPort() {
        return port;
    }
    public static void main(String[] args) throws IOException {
        WebServer webServer = new WebServer();
        ServerSocket serverSocket = new ServerSocket(webServer.getPort());
        System.out.println("Listening for connections on port 6789...\r\n");

        // Listen for new client connections
        while(true) {

            // Accept new client connection
            Socket connectionSocket = serverSocket.accept();

            // Create new thread to handle client request
            Thread connectionThread = new Thread(new Connection(connectionSocket));

            // Start the connection thread
            connectionThread.start();
            System.out.println("New connection on port 6789...\r\n");
        }
    }
   
}
