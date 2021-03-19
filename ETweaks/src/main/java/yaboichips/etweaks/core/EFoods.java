package yaboichips.etweaks.core;

import net.minecraft.item.Food;
import net.minecraft.util.ResourceLocation;
import yaboichips.etweaks.ETweaks;

import java.util.ArrayList;
import java.util.List;

public class EFoods {

    public static List<Food> foods = new ArrayList<>();


    public static final Food PICKLE = (new Food.Builder()).hunger(4).saturation(0.3F).fastToEat().build();
    public static final Food SUPERMEAL = (new Food.Builder()).hunger(7).saturation(2.4F).build();

}
