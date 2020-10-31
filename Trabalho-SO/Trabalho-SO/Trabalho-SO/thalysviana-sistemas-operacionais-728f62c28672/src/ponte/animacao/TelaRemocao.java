package ponte.animacao;

import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import ponte.controle.Ponte;

public class TelaRemocao {

	public static void display() {
		
		Stage stage = new Stage();
		Group raiz = new Group();
		
		VBox container = new VBox(25);
		container.setTranslateX(40);
		container.setTranslateY(40);
		
		HBox remocao = new HBox(20);
		javafx.scene.control.TextField campoRemocao = new TextField();
		remocao.getChildren().addAll(new Label("Carro ID"), campoRemocao);
		
		Button btnRemove = new Button("Remover");
		btnRemove.setOnAction(e -> {
			
			int idCarro = Integer.parseInt(campoRemocao.getText()) + 1;
			TelaAnimacao.getRaiz().getChildren().remove(Ponte.carrosView.get(idCarro)); 
		});
		
		container.getChildren().addAll(remocao, btnRemove);
		raiz.getChildren().add(container);
		
		Scene cena = new Scene(raiz, 300, 150);
		stage.setTitle("Remover carros");
		stage.setScene(cena);
		stage.show();
	}
	

}
