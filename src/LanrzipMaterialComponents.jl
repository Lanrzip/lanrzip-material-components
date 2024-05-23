
module LanrzipMaterialComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_lanrzipmaterialcomponents.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "lanrzip_material_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "lanrzip_material_components.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "lanrzip_material_components.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
