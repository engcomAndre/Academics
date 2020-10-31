package ponte.animacao;

import javafx.animation.Interpolator;
import javafx.animation.Transition;
import javafx.geometry.Rectangle2D;
import javafx.scene.image.ImageView;
import javafx.util.Duration;

public class AnimacaoSprite extends Transition{
	private final ImageView imgView;
    private final int cont;
    private final int colunas;
    private final int offsetX;
    private final int offsetY;
    private final int largura;
    private final int altura;

    private int ultimoIndex;

    public AnimacaoSprite(
            ImageView imgView, 
            Duration duracao, 
            int cont,   int colunas,
            int offsetX, int offsetY,
            int largura,   int altura) {
        this.imgView   = imgView;
        this.cont      = cont;
        this.colunas   = colunas;
        this.offsetX   = offsetX;
        this.offsetY   = offsetY;
        this.largura   = largura;
        this.altura    = altura;
        setCycleDuration(duracao);
        setInterpolator(Interpolator.LINEAR);
    }

    protected void interpolate(double k) {
        final int index = Math.min((int) Math.floor(k * cont), cont - 1);
        if (index != ultimoIndex) {
            final int x = (index % colunas) * largura  + offsetX;
            final int y = (index / colunas) * altura + offsetY;
            imgView.setViewport(new Rectangle2D(x, y, largura, altura));
            ultimoIndex = index;
        }
    }
}
