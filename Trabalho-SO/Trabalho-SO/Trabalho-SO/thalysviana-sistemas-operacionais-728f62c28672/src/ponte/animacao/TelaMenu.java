package ponte.animacao;

import java.util.Random;
import javafx.animation.TranslateTransition;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleGroup;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import ponte.carro.CarroLeste;
import ponte.carro.CarroOeste;
import ponte.carro.Sentido;
import ponte.controle.Ponte;

public class TelaMenu {
	
	public static void display() {
		
		Stage stage = new Stage();
		StackPane raiz = new StackPane(); 
		
		VBox container = new VBox(25);
		container.setTranslateX(40);
		container.setTranslateY(40);
		
		// Botões de prioridade
		HBox prioridades = new HBox(20);
		RadioButton radioLeste = new RadioButton("Leste");
		RadioButton radioOeste = new RadioButton("Oeste");
		RadioButton radioNenhuma = new RadioButton("Nenhuma");
		radioLeste.setSelected(true);
		
		ToggleGroup radioPrioridades = new ToggleGroup();
		radioPrioridades.getToggles().addAll(radioLeste, radioOeste, radioNenhuma);
		prioridades.getChildren().addAll(new Label("Prioridades"), radioLeste, radioOeste, radioNenhuma);
		
		// Tempos de permanência e travessia
		HBox tempos = new HBox(20);
		Label lblPermanencia = new Label("Permanência");
		Label lblTravessia = new Label("Travessia");
		TextField campoPermanencia = new TextField();
		TextField campoTravessia = new TextField();
		tempos.getChildren().addAll(lblPermanencia, campoPermanencia, lblTravessia, campoTravessia);
		
		// Botões de configuração
		HBox botoes = new HBox(20);
		Button btnPrioridade = new Button("Define Prioridade");
		Button btnCarroLeste = new Button("Carro Leste");
		Button btnCarroOeste = new Button("Carro Oeste");
		Button btnRemoveCarro = new Button("Remover Carro");
		botoes.getChildren().addAll(btnPrioridade, btnCarroOeste, btnCarroLeste, btnRemoveCarro);
		
		// Define prioridade
		btnPrioridade.setOnAction(e -> {
			RadioButton prioridade = (RadioButton) radioPrioridades.getSelectedToggle();
			String txt = "";
			
			if (prioridade.getText() == "Leste"){
				Ponte.prioridadeDefinida = Sentido.LESTE;
				txt = "Leste";
			}
			else if (prioridade.getText() == "Oeste") {
				Ponte.prioridadeDefinida = Sentido.OESTE;
				txt = "Oeste";
			}
			else {
				Ponte.prioridadeDefinida = Sentido.NENHUM;
				txt = "Nenhuma";
			}
			System.out.println("Prioridade definida: " + txt);
		});
		
		btnCarroLeste.setOnAction(e -> {
			int tempoPermanencia = Integer.parseInt(campoPermanencia.getText());
			int tempoTravessia = Integer.parseInt(campoTravessia.getText());
			new CarroLeste(Ponte.idCarro, tempoPermanencia, tempoTravessia).start();
			TelaMenu.insereCarroAnimacao(Sentido.OESTE, tempoPermanencia, tempoTravessia);
		});
		
		btnCarroOeste.setOnAction(e -> {
			int tempoPermanencia = Integer.parseInt(campoPermanencia.getText());
			int tempoTravessia = Integer.parseInt(campoTravessia.getText());
			new CarroOeste(Ponte.idCarro, tempoPermanencia, tempoTravessia).start();
			TelaMenu.insereCarroAnimacao(Sentido.LESTE, tempoPermanencia, tempoTravessia);
		});
		
		btnRemoveCarro.setOnAction(e -> {
			TelaRemocao.display();
		});
		
		container.getChildren().addAll(prioridades, tempos, botoes);
		raiz.getChildren().addAll(container);
		
		Scene cena = new Scene(raiz, 550, 200);
		stage.setTitle("Definição de parâmetros");
		stage.setScene(cena);
		stage.show();
		
	}
	
	public static void insereCarroAnimacao(Sentido sentido,int tempoPermanencia, int tempoTravessia) {
		
		Image imagem = TelaMenu.escolheCarro(sentido);
		ImageView view = new ImageView(imagem);
		TelaAnimacao.getRaiz().getChildren().addAll(view);
		TelaAnimacao.animaCarro(view).play();
		TranslateTransition translate = TelaAnimacao.andaCarro(view, sentido, tempoPermanencia, tempoTravessia);
		Ponte.idCarro++;
		Ponte.carrosView.put(Ponte.idCarro, view);
		Ponte.translates.put(Ponte.idCarro, translate);
	}
	
	public static Image escolheCarro(Sentido sentido) {
		Image[] carroEsq = { TelaAnimacao.TRICOLOR_ESQ, TelaAnimacao.AZUL_ESQ, TelaAnimacao.BRANCO_ESQ, TelaAnimacao.VERMELHO_ESQ };
		Image[] carroDir = { TelaAnimacao.TRICOLOR_DIR, TelaAnimacao.AZUL_DIR, TelaAnimacao.BRANCO_DIR, TelaAnimacao.VERMELHO_DIR};
		
		Random index = new Random();
		
		if (sentido == Sentido.OESTE)
			return carroEsq[index.nextInt(4)];
		else
			return carroDir[index.nextInt(4)];
	}
	
}
