package yaboichips.etweaks;

import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.item.Item;
import net.minecraft.util.ResourceLocation;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.InterModComms;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.event.lifecycle.InterModEnqueueEvent;
import net.minecraftforge.fml.event.lifecycle.InterModProcessEvent;
import net.minecraftforge.fml.event.server.FMLServerStartingEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import yaboichips.etweaks.core.EBlocks;
import yaboichips.etweaks.core.EItems;

import javax.annotation.Nonnull;
import java.util.stream.Collectors;

// The value here should match an entry in the META-INF/mods.toml file
@Mod(ETweaks.MOD_ID)
public class ETweaks {

    public static final String MOD_ID = "etweaks";
    private static final Logger LOGGER = LogManager.getLogger();

    public ETweaks() {
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::setup);
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::enqueueIMC);
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::processIMC);
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::doClientStuff);

        MinecraftForge.EVENT_BUS.register(this);
    }

    private void setup(final FMLCommonSetupEvent event) {
        LOGGER.info("HELLO FROM PREINIT");
        LOGGER.info("DIRT BLOCK >> {}", Blocks.DIRT.getRegistryName());
    }

    private void doClientStuff(final FMLClientSetupEvent event) {
        LOGGER.info("Got game settings {}", event.getMinecraftSupplier().get().gameSettings);
    }

    private void enqueueIMC(final InterModEnqueueEvent event) {
        InterModComms.sendTo("etweaks", "helloworld", () -> {
            LOGGER.info("Hello world from the MDK");
            return "Hello world";
        });
    }

    private void processIMC(final InterModProcessEvent event) {
        LOGGER.info("Got IMC {}", event.getIMCStream().
                map(m -> m.getMessageSupplier().get()).
                collect(Collectors.toList()));
    }

    public static @Nonnull
    ResourceLocation createResource(String path) {
        return new ResourceLocation(MOD_ID, path);
    }

    @SubscribeEvent
    public void onServerStarting(FMLServerStartingEvent event) {
        LOGGER.info("HELLO from server starting");
    }

    @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
    public static class RegistryEvents {
        @SubscribeEvent
        public static void registerBlocks(final RegistryEvent.Register<Block> event) {
            LOGGER.info("HELLO from Register Block");
            EBlocks.init();
            EBlocks.blocks.forEach(block -> event.getRegistry().register(block));
            EBlocks.blocks.clear();
            EBlocks.blocks = null;
            LOGGER.info("GeckoMod: Blocks registered!");
        }

        @SubscribeEvent
        public static void registerItems(RegistryEvent.Register<Item> event) {
            LOGGER.debug("GeckoMod: Registering items...");
            EItems.init();
            EItems.items.forEach(item -> event.getRegistry().register(item));
            EItems.items.clear();
            EItems.items = null;
            LOGGER.info("GeckoMod: Items registered!");
        }
    }

    /* Notes:
    Editable Signs
    No Fall Damage Apple
    Time Set Day/Night Staff
    Step up apple
    Pockets
    Rocket Boots
    -Super Saturating Food-
    -Villager Traps-
    -Edible Pickles-
    Reusable Ender Pearl
    Float Resistance
    Wither Resistance
    Repairable Anvil
    Ground Beef
    Meatloaf
    Cool Cake
    Stiff Scaffolding
    Zoom Pickaxe
    Coloured Lamps
    Coloured Torches
    Coloured Endrods
    Banner Duplicator
    Reddit Gold/Silver Awards
    Blender
    Juices
    I'm Waking Up Music Disc
     */

}
