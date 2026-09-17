"""168 unique photoreal prompts: 21 LED series x 8 frames."""
from __future__ import annotations

STYLE = (
    "Photoreal commercial LED display catalog photography, cinematic lighting, "
    "no logos, no brand names, no readable text, no Chinese characters, no watermarks, "
    "no GKGD, no Qiangli, no 9thPanel, no UI overlays, no fake certificates."
)
STUDIO = STYLE + " Clean grey-white photo studio, product shot, shallow depth of field."
SCENE = STYLE + " Istanbul or European city, luxury architectural photography."

KEYS = ("hero", "studio", "feat-1", "feat-2", "feat-3", "feat-4", "use-1", "use-2")

PACKS: dict[str, dict[str, tuple[str, str]]] = {
    "cms-series-crystal-film-display": {
        "hero": ("16:9", SCENE + " Luxury Nisantasi boutique glass facade with transparent LED film; mannequins still visible through colorful night graphics."),
        "studio": ("4:3", STUDIO + " Ultra-thin transparent LED film sheet on a glass sample stand, edge showing millimetre thickness."),
        "feat-1": ("16:9", SCENE + " Daytime shop window: handbags visible behind transparent LED film with a soft abstract graphic overlay."),
        "feat-2": ("4:3", SCENE + " Technician applying a thin LED crystal film onto existing glass, profile shot emphasizing how thin the layer is."),
        "feat-3": ("16:9", SCENE + " Night retail facade, high-contrast colorful LED film advertisement, street reflections on glass."),
        "feat-4": ("4:3", SCENE + " Service: technician swapping a modular LED film strip on a glass wall, tools on a cart."),
        "use-1": ("16:9", SCENE + " Automotive showroom glass wall with transparent LED film and a car visible behind."),
        "use-2": ("16:9", SCENE + " Hotel lobby atrium glass with a slim transparent LED information band."),
    },
    "hs-series-holographic-display": {
        "hero": ("16:9", SCENE + " Product launch stage, holographic LED mesh curtain, a car silhouette visible through the mesh, dramatic spotlights."),
        "studio": ("4:3", STUDIO + " Holographic LED mesh panel hanging, see-through grid of SMD pixels, black backdrop."),
        "feat-1": ("4:3", STUDIO + " Extreme close-up of see-through LED mesh weave, pixels on thin wires, background bokeh."),
        "feat-2": ("16:9", SCENE + " Fashion launch: floating graphics on holographic LED with models walking behind the mesh."),
        "feat-3": ("4:3", SCENE + " Lightweight holographic LED cabinet clipped to a concert truss, empty venue."),
        "feat-4": ("16:9", SCENE + " Camera operator filming a holographic LED wall, no flicker, studio lights."),
        "use-1": ("16:9", SCENE + " Automotive reveal behind holographic LED mesh in a dark showroom."),
        "use-2": ("16:9", SCENE + " Brand experience room with holographic LED and a physical product on a plinth behind it."),
    },
    "q-mini-series": {
        "hero": ("16:9", SCENE + " Compact fine-pitch LED video wall in a small Istanbul meeting room, 6 people at a table, sharp slides."),
        "studio": ("4:3", STUDIO + " Tiny die-cast mini LED cabinet, front view, fine pixel pitch visible, matte black."),
        "feat-1": ("4:3", STUDIO + " Macro of 1.5mm fine pitch LED module, uniform black surface, studio light."),
        "feat-2": ("16:9", SCENE + " Mini LED cabinets fitted into a narrow office niche beside a glass door."),
        "feat-3": ("16:9", SCENE + " Quiet boardroom with mini LED wall, no visible fans, calm corporate interior."),
        "feat-4": ("16:9", SCENE + " Dimmed meeting room, mini LED wall showing a dark gradient without banding."),
        "use-1": ("16:9", SCENE + " Control niche with compact mini LED wall and operator desk."),
        "use-2": ("16:9", SCENE + " Showroom demo of Q Mini cabinet next to a larger wall, comparison."),
    },
    "nc-series": {
        "hero": ("16:9", SCENE + " Broadcast studio with COB fine-pitch LED backdrop, cameras, dark set."),
        "studio": ("4:3", STUDIO + " COB LED module close-up, smooth encapsulated surface, no exposed beads."),
        "feat-1": ("4:3", STUDIO + " Finger almost touching a durable COB LED surface, impact-resistant look."),
        "feat-2": ("16:9", SCENE + " Thermal: rear of COB cabinet with neat heat path, low-profile, studio."),
        "feat-3": ("16:9", SCENE + " TV studio LED wall with deep blacks, camera in foreground, no flicker."),
        "feat-4": ("4:3", STUDIO + " Uniform COB LED tiles in a grid, identical color, quality control bench."),
        "use-1": ("16:9", SCENE + " Corporate lobby COB LED wall, people walking close, no smashed pixels."),
        "use-2": ("16:9", SCENE + " News studio virtual set with COB LED floor-to-wall."),
    },
    "indoor-q-series": {
        "hero": ("16:9", SCENE + " Five-star Istanbul hotel lobby with a large fine-pitch indoor LED wall showing abstract blue art, Bosphorus light through windows."),
        "studio": ("4:3", STUDIO + " Indoor fixed LED cabinet 500mm class, die-cast, front service magnets, matte black."),
        "feat-1": ("16:9", SCENE + " Hotel lobby LED wall dimmed for daytime, PWM smooth brightness, guests walking."),
        "feat-2": ("16:9", SCENE + " Exhibition booth indoor LED wall being filmed by a camera, high refresh, no scan lines."),
        "feat-3": ("16:9", SCENE + " Dark hotel bar, indoor LED wall with 16-bit smooth greys and cinematic content."),
        "feat-4": ("4:3", STUDIO + " Color-matched LED modules on a calibration jig, uniform batch, lab lighting."),
        "use-1": ("16:9", SCENE + " Corporate plaza lobby indoor LED welcome wall, 8 metre viewing."),
        "use-2": ("16:9", SCENE + " Retail atrium indoor LED wall with wide viewing angle, shoppers below."),
    },
    "pdc-series": {
        "hero": ("16:9", SCENE + " 24/7 command-and-control room, dense fine-pitch LED videowall, operators at consoles."),
        "studio": ("4:3", STUDIO + " Pro fine-pitch LED cabinet labeled-free, front-service, dark grey."),
        "feat-1": ("16:9", SCENE + " Night operations center, LED wall on a low-brightness 24/7 profile."),
        "feat-2": ("4:3", STUDIO + " Three Pro pitch modules 0.9 1.2 1.5mm side by side on a bench."),
        "feat-3": ("16:9", SCENE + " Technician servicing LED wall from the front in a narrow corridor."),
        "feat-4": ("16:9", SCENE + " Silent cooling: rear of control-room LED cabinets, no roaring fans."),
        "use-1": ("16:9", SCENE + " Traffic control room LED wall, maps and camera feeds, no logos."),
        "use-2": ("16:9", SCENE + " Executive situation room, fine-pitch LED, mahogany table."),
    },
    "mk-series": {
        "hero": ("16:9", SCENE + " Shopping mall atrium with a curved indoor LED ribbon wrapping a column."),
        "studio": ("4:3", STUDIO + " Flexible indoor LED module bent in a gentle curve, studio."),
        "feat-1": ("16:9", SCENE + " Concave LED feature wall in a flagship store, seamless curve."),
        "feat-2": ("16:9", SCENE + " 90-degree LED corner with no visible gap, retail interior."),
        "feat-3": ("16:9", SCENE + " Brand wall in a mall, magnetic LED modules being clicked on."),
        "feat-4": ("4:3", SCENE + " Installer placing magnetic LED tiles quickly on a curved frame."),
        "use-1": ("16:9", SCENE + " Luxury retail curved LED around a circular display island."),
        "use-2": ("16:9", SCENE + " Museum exhibition with inner-curve LED immersion."),
    },
    "indoor-r-series": {
        "hero": ("16:9", SCENE + " Government conference hall with a stable indoor LED wall, flags, wooden desks."),
        "studio": ("4:3", STUDIO + " Robust indoor LED cabinet on a floor stand, institutional grey."),
        "feat-1": ("16:9", SCENE + " University lecture hall LED wall, wide seating, presentation content without text."),
        "feat-2": ("16:9", SCENE + " LED wall on wall-mount and a matching floor-stand unit in a training room."),
        "feat-3": ("16:9", SCENE + " Two adjacent indoor LED walls color-matched, council chamber."),
        "feat-4": ("4:3", SCENE + " Spare LED modules on a Turkish warehouse shelf, labeled boxes without brands."),
        "use-1": ("16:9", SCENE + " Corporate training room indoor LED, horseshoe tables."),
        "use-2": ("16:9", SCENE + " Municipal meeting room indoor LED, daylight through blinds."),
    },
    "cs-series": {
        "hero": ("16:9", SCENE + " Private cinema with a high-contrast indoor LED screen, dark room, wide seats."),
        "studio": ("4:3", STUDIO + " High-contrast indoor LED cabinet, deep black face, studio."),
        "feat-1": ("16:9", SCENE + " Cinema LED screen showing a dark night scene with true blacks."),
        "feat-2": ("16:9", SCENE + " Wide auditorium LED, side seats still seeing the image, no color shift."),
        "feat-3": ("16:9", SCENE + " Silent cinema: LED wall, no projector fan, audience silhouette."),
        "feat-4": ("16:9", SCENE + " HDR-like LED content in a screening room, highlights and shadows."),
        "use-1": ("16:9", SCENE + " Hotel ballroom cinema LED for a gala, dark drapes."),
        "use-2": ("16:9", SCENE + " Corporate screening room LED, leather chairs."),
    },
    "n-series": {
        "hero": ("16:9", SCENE + " Broadcast LED floor and wall, presenter standing on LED floor, cameras."),
        "studio": ("4:3", STUDIO + " Narrow-pixel LED floor tile with reinforced surface, studio."),
        "feat-1": ("16:9", SCENE + " Camera close-up of N-series LED wall, broadcast lighting, no moire."),
        "feat-2": ("4:3", STUDIO + " Fine pitch LED module extreme close-up, dense pixels."),
        "feat-3": ("16:9", SCENE + " LED floor with dancers, load-bearing tiles, concert rehearsal."),
        "feat-4": ("4:3", STUDIO + " Calibration camera over LED modules on a jig."),
        "use-1": ("16:9", SCENE + " Virtual production volume, LED wall and ceiling, dark stage."),
        "use-2": ("16:9", SCENE + " Sports studio LED floor graphic, presenter, no logos."),
    },
    "rw-series": {
        "hero": ("16:9", SCENE + " Open-air Istanbul concert, large rental LED wall, crowd, night, fast-lock cabinets."),
        "studio": ("4:3", STUDIO + " Rental LED cabinet with quick-lock hardware, curve-capable, flight-case nearby."),
        "feat-1": ("4:3", SCENE + " Hands locking rental LED cabinets together with pins, load-in."),
        "feat-2": ("16:9", SCENE + " Indoor rental LED 2.9mm and outdoor 3.9mm walls in one warehouse comparison."),
        "feat-3": ("16:9", SCENE + " Black flight cases lined up backstage, rental LED tour logistics."),
        "feat-4": ("16:9", SCENE + " Concert IMAG LED, cameras, high refresh, no flicker."),
        "use-1": ("16:9", SCENE + " Festival main stage rental LED, truss fly."),
        "use-2": ("16:9", SCENE + " Indoor concert rental LED curved wall."),
    },
    "cg-series": {
        "hero": ("16:9", SCENE + " Three-sided exhibition booth with lightweight carbon-look rental LED walls."),
        "studio": ("4:3", STUDIO + " Ultra-light rental LED cabinet, carbon-look finish, on a scale aesthetic."),
        "feat-1": ("16:9", SCENE + " LED wall hanging from truss at a fair, slim cabinets, low load."),
        "feat-2": ("16:9", SCENE + " Expo booth build: three LED facades, two-day install look."),
        "feat-3": ("16:9", SCENE + " Night strike: crew dismantling rental LED after a fair close."),
        "feat-4": ("4:3", SCENE + " Hot-swap: technician exchanging a rental LED module in seconds."),
        "use-1": ("16:9", SCENE + " Auto show booth with lightweight rental LED."),
        "use-2": ("16:9", SCENE + " Tech fair island booth, hanging LED banners."),
    },
    "ln-series": {
        "hero": ("16:9", SCENE + " Concert main LED plus side IMAG wings, linear rental cabinets, night."),
        "studio": ("4:3", STUDIO + " Linear rental LED cabinet, wide format, quick locks."),
        "feat-1": ("16:9", SCENE + " Main LED wall behind a band, IMAG screens on sides."),
        "feat-2": ("16:9", SCENE + " Linear LED wings extending a stage, clean lines."),
        "feat-3": ("16:9", SCENE + " Outdoor festival LED with weather covers, IP-ready rental."),
        "feat-4": ("4:3", SCENE + " Fast lock of LN cabinets stacking on stage."),
        "use-1": ("16:9", SCENE + " Automotive launch arena, linear LED backdrop."),
        "use-2": ("16:9", SCENE + " Open-air festival night, LED wall flying on motors."),
    },
    "dm-series": {
        "hero": ("16:9", SCENE + " TV show set with slim-frame rental LED wall, modern bezel-less look."),
        "studio": ("4:3", STUDIO + " Thin-frame rental LED cabinet, modern edge, studio."),
        "feat-1": ("16:9", SCENE + " Fashion TV set, slim LED wall, elegant lighting."),
        "feat-2": ("16:9", SCENE + " Multi-camera TV studio, high-refresh LED, no flicker on monitors."),
        "feat-3": ("16:9", SCENE + " Crew carrying lightweight DM cabinets into a studio."),
        "feat-4": ("16:9", SCENE + " Front and rear service on a slim rental LED wall."),
        "use-1": ("16:9", SCENE + " Talk-show LED backdrop, audience seats."),
        "use-2": ("16:9", SCENE + " Touring TV set packed, slim cabinets in cases."),
    },
    "pm-series": {
        "hero": ("16:9", SCENE + " Rental warehouse: LED panels, spare modules, labeled flight cases, tour prep."),
        "studio": ("4:3", STUDIO + " Rental LED panel with a spare module pulled out, hot-swap design."),
        "feat-1": ("4:3", SCENE + " Technician swapping a module on a live rental wall in seconds."),
        "feat-2": ("16:9", SCENE + " Flight-case sets opened, foam-cut LED modules, truck dock."),
        "feat-3": ("4:3", STUDIO + " Close-up of rental lock pins and latches."),
        "feat-4": ("16:9", SCENE + " Mixed indoor and outdoor rental LED stacks in one shop."),
        "use-1": ("16:9", SCENE + " Load-in of spare-heavy rental package at a venue."),
        "use-2": ("16:9", SCENE + " Tour truck packed with PM flight cases."),
    },
    "outdoor-q-series": {
        "hero": ("16:9", SCENE + " Istanbul avenue digital billboard, high-brightness outdoor LED, sunny day, readable image."),
        "studio": ("4:3", STUDIO + " Outdoor LED cabinet, die-cast aluminium, rear service door, no logos."),
        "feat-1": ("16:9", SCENE + " South-facing mall facade LED in harsh noon sun, still bright and readable."),
        "feat-2": ("4:3", SCENE + " Rain on an IP-rated outdoor LED cabinet, water beading, sealed gaskets."),
        "feat-3": ("16:9", SCENE + " DOOH control room screens monitoring a remote outdoor LED, no brand UI."),
        "feat-4": ("4:3", STUDIO + " Aluminium outdoor cabinet heatsink fins, thermal design."),
        "use-1": ("16:9", SCENE + " Bus-stop outdoor LED, pedestrians, daylight."),
        "use-2": ("16:9", SCENE + " Shopping mall media facade at dusk."),
    },
    "outdoor-s-series": {
        "hero": ("16:9", SCENE + " Football stadium peri-LED ribbon and a large outdoor LED, match day, no team logos."),
        "studio": ("4:3", STUDIO + " Heavy-duty stadium outdoor LED cabinet, rear corridor handles."),
        "feat-1": ("16:9", SCENE + " Long-distance stadium LED readable from upper stands."),
        "feat-2": ("16:9", SCENE + " Wind and vibration: LED cabinets on a stadium gantry, structural steel."),
        "feat-3": ("16:9", SCENE + " Technician in a rear service corridor behind stadium LED."),
        "feat-4": ("16:9", SCENE + " Daytime match, high-nit stadium LED showing abstract crowd graphics."),
        "use-1": ("16:9", SCENE + " Peri-LED around the pitch, daylight."),
        "use-2": ("16:9", SCENE + " Large format roadside DOOH, S-series cabinets."),
    },
    "qm-series": {
        "hero": ("16:9", SCENE + " Slim 640x480 aluminium LED cabinets forming a thin indoor wall, architectural slot."),
        "studio": ("4:3", STUDIO + " Slim aluminium 640 by 480 LED cabinet, side profile showing thin depth."),
        "feat-1": ("16:9", SCENE + " LED wall almost flush with plasterboard, thin cabinet depth."),
        "feat-2": ("4:3", STUDIO + " Standard module seating in a 640x480 cabinet, open rear."),
        "feat-3": ("16:9", SCENE + " Semi-outdoor canopy LED using slim cabinets, daylight."),
        "feat-4": ("16:9", SCENE + " Ceiling-hung slim LED banners in a museum."),
        "use-1": ("16:9", SCENE + " Column wrap with slim QM cabinets in a lobby."),
        "use-2": ("16:9", SCENE + " Retail slot wall, thin LED, hanging clothes nearby."),
    },
    "mg-series": {
        "hero": ("16:9", SCENE + " Street digital billboard with die-cast outdoor cabinets, 320x160 modules visible at edge."),
        "studio": ("4:3", STUDIO + " Die-cast outdoor LED cabinet with 320x160 modules, rear cover open."),
        "feat-1": ("4:3", STUDIO + " Water-and-dust sealed outdoor cabinet gasket close-up."),
        "feat-2": ("4:3", STUDIO + " Grid of 320x160 outdoor LED modules on a bench."),
        "feat-3": ("16:9", SCENE + " City bus-stop and billboard MG cabinets, traffic bokeh."),
        "feat-4": ("16:9", SCENE + " Rear door open, technician servicing outdoor LED PSU."),
        "use-1": ("16:9", SCENE + " Highway billboard, MG cabinets, golden hour."),
        "use-2": ("16:9", SCENE + " Urban square totem LED, pedestrians."),
    },
    "p-series": {
        "hero": ("16:9", SCENE + " LED project spare kit: redundant PSUs, cables, connectors on a workbench, warehouse."),
        "studio": ("4:3", STUDIO + " LED power supply units and cabinet accessories, neat product lineup, no logos."),
        "feat-1": ("4:3", STUDIO + " Dual redundant LED PSU in a cabinet slot, N+1."),
        "feat-2": ("16:9", SCENE + " Matching PSU and cabinet parts next to indoor and rental cabinets."),
        "feat-3": ("4:3", STUDIO + " Quick-connect LED power and data cables, coiled."),
        "feat-4": ("16:9", SCENE + " Istanbul warehouse shelves of spare PSUs ready to ship."),
        "use-1": ("16:9", SCENE + " 24/7 LED wall rear, extra PSU installed."),
        "use-2": ("16:9", SCENE + " Rental case of spare PSUs at a venue."),
    },
    "v-series-": {
        "hero": ("16:9", SCENE + " Indoor LED totem columns in a mall, vertical creative screens, shoppers."),
        "studio": ("4:3", STUDIO + " Vertical LED totem cabinet, slim, clip service, studio."),
        "feat-1": ("16:9", SCENE + " Pair of LED totems flanking a hotel entrance."),
        "feat-2": ("16:9", SCENE + " Creative irregular LED shape on a brand wall, custom frame."),
        "feat-3": ("16:9", SCENE + " Lightweight hanging vertical LED inside a glass atrium."),
        "feat-4": ("4:3", SCENE + " Fast clips: opening a totem for service in a shop window."),
        "use-1": ("16:9", SCENE + " Wayfinding LED totems in an airport-like hall, no logos."),
        "use-2": ("16:9", SCENE + " Retail window LED totem, night, street outside."),
    },
}

SLUGS = list(PACKS.keys())


def jobs() -> list[dict]:
    out = []
    idx = 0
    for slug in SLUGS:
        for key in KEYS:
            ratio, prompt = PACKS[slug][key]
            out.append({"index": idx, "slug": slug, "key": key, "aspect_ratio": ratio, "prompt": prompt})
            idx += 1
    return out
