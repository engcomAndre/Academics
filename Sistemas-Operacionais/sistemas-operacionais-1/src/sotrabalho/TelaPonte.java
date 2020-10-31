package sotrabalho;

import java.awt.Rectangle;

import javafx.animation.Interpolator;
import javafx.animation.Timeline;
import javafx.animation.TranslateTransition;
import javafx.animation.TranslateTransitionBuilder;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.RectangleBuilder;
import javafx.stage.Stage;
import javafx.util.Duration;

public class TelaPonte extends Application {
	
	private String ponteImagem = getClass().getResource("/assets/ponteFinal.png").toString();
	private String carroVEsqImagem = getClass().getResource("/assets/vermelho-para-esquerda.png").toString();
	private String carroVDirImagem = getClass().getResource("/assets/vermelho-para-direita.png").toString();
	private String carroAEsqImagem = getClass().getResource("/assets/azul-para-esquerda.png").toString();
	private String carroADirImagem = getClass().getResource("/assets/azul-para-direita.png").toString();
	private String carroBEsqImagem = getClass().getResource("/assets/branco-para-esquerda.png").toString();
	private String carroBDirImagem = getClass().getResource("/assets/branco-para-direita.png").toString();
	
	TranslateTransition translate;
	TranslateTransition translateTest;
	javafx.scene.shape.Rectangle rect;
	
	
	@Override
	public void start(Stage palco) {
		
		// Cria a view da ponte
		Image ponte = new Image(ponteImagem);
		ImageView ponteView = new ImageView(ponte);
		
		
		// Cria as views dos carros
		Image carroVEsq = new Image(carroVEsqImagem);
		ImageView carroVEsqView = new ImageView(carroVEsq);
		ImageView carroTestView = new ImageView(carroVEsq);
		
		// Carro L-O
		carroVEsqView.setTranslateY(-20);
		carroVEsqView.setTranslateX(500);
		
		// Carro O-L
		carroTestView.setTranslateY(-30);
		carroTestView.setTranslateX(-500);
	
		
		translate = TranslateTransitionBuilder
					.create()
					.duration(new Duration(20*1000))
					.node(carroVEsqView)
					.toX(-400)
					.autoReverse(true)
					.cycleCount(Timeline.INDEFINITE)
					.interpolator(Interpolator.EASE_BOTH)
					.build();
		
		translateTest = TranslateTransitionBuilder
				.create()
				.duration(new Duration(20*1000))
				.node(carroTestView)
				.toX(600)
				.autoReverse(true)
				.cycleCount(Timeline.INDEFINITE)
				.interpolator(Interpolator.EASE_BOTH)
				.build();
		
		
		StackPane raiz = new StackPane();
		raiz.getChildren().addAll(ponteView, carroVEsqView, carroTestView);
		
		Scene cena = new Scene(raiz, 1500, 700);
		
		palco.setTitle("Teste");
		palco.setScene(cena);
		palco.show();
		
		translateTest.play();
		translate.play();
		
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
	
}
