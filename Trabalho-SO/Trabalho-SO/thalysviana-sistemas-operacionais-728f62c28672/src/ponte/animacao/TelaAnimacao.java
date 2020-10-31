package ponte.animacao;

import javafx.animation.Animation;
import javafx.animation.TranslateTransition;
import javafx.application.Application;
import javafx.geometry.Rectangle2D;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Duration;
import ponte.carro.Sentido;

public class TelaAnimacao extends Application {
	
	public static final Image TRICOLOR_ESQ = new Image(TelaAnimacao.class.getResource("/assets/tricolorEsq.png").toString());
	public static final Image TRICOLOR_DIR = new Image(TelaAnimacao.class.getResource("/assets/tricolorDir.png").toString());
	public static final Image AZUL_ESQ = new Image(TelaAnimacao.class.getResource("/assets/azulEsq.png").toString());
	public static final Image AZUL_DIR = new Image(TelaAnimacao.class.getResource("/assets/azulDir.png").toString());
	public static final Image VERMELHO_ESQ = new Image(TelaAnimacao.class.getResource("/assets/vermelhoEsq.png").toString());
	public static final Image VERMELHO_DIR = new Image(TelaAnimacao.class.getResource("/assets/vermelhoDir.png").toString());
	public static final Image BRANCO_ESQ = new Image(TelaAnimacao.class.getResource("/assets/brancoEsq.png").toString());
	public static final Image BRANCO_DIR = new Image(TelaAnimacao.class.getResource("/assets/brancoDir.png").toString());
    public static final Image PONTE = new Image(TelaAnimacao.class.getResource("/assets/ponteFinal.png").toString());
   
    private static final int COLUNAS = 2;
    private static final int CONT = 2;
    private static final int OFFSET_X = 18;
    private static final int OFFSET_Y = 0;
    private static final int LARGURA = 400; // 400
    private static final int ALTURA = 148; // 148
    
    private static StackPane raiz;

    public static void main(String[] args) {
        launch(args);
    }
    
    public static StackPane getRaiz() {
    	return raiz;
    }
    
    public static Animation animaCarro(ImageView view) {
    	
    	view.setViewport(new Rectangle2D(OFFSET_X, OFFSET_Y, LARGURA, ALTURA));
        view.setTranslateY(-40);  
    	Animation animation = new AnimacaoSprite(
                view,
                Duration.millis(200),
                CONT, COLUNAS,
                OFFSET_X, OFFSET_Y,
                LARGURA, ALTURA
        );
        animation.setCycleCount(Animation.INDEFINITE);
        return animation;
    }
    
    public static TranslateTransition andaCarro(ImageView view, Sentido sentido, int tempoPermanencia, int tempoTravessia) {
    	
    	int fim;
    	if (sentido == Sentido.OESTE) {
    		view.setTranslateX(700);
    		fim = -900;
    	} else {
    		view.setTranslateX(-700);
    		fim = 900;
    	}  

        TranslateTransition translate = new TranslateTransition();
        translate.setNode(view);
        translate.setToX(fim);
        translate.setDuration(new Duration(tempoTravessia * 500));
        
        return translate;
    }
    
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Testando Animacao");
        
        raiz = new StackPane();
        
        final ImageView ponteView = new ImageView(PONTE);           
        
        javafx.scene.control.Button btnConfigura = new javafx.scene.control.Button("Configuração");
        raiz.getChildren().addAll(ponteView, btnConfigura);
        
        btnConfigura.setOnAction(e -> {
        	TelaMenu.display();
        });
        btnConfigura.setTranslateX(600);
        btnConfigura.setTranslateY(250);
        
        primaryStage.setScene(new Scene(raiz, 1400, 700));
        primaryStage.show();
        
    }
    
}
